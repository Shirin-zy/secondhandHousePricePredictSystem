import pandas as pd
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import numpy as np
from flask_cors import CORS
import random
import string
import pandas as pd
import numpy as np
import pickle
import re
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import xgboost as xgb
import lightgbm as lgb
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
app = Flask(__name__)
CORS(app)

# 查询小区房价信息接口
@app.route('/info/area',methods=['get'])
def areainfo():
    print('查询该小区信息')
    data = pd.read_csv('../data/deal/total_fordraw.csv', index_col=0)
    areaname = request.args.get('area', '', type=str)
    # areaname = '高钱塘一品'
    select = data[data['小区名称'] == areaname]
    averagetotalprice = int(select['总价'].mean())
    averageprice = int(select['单价'].mean())
    averageattention = int(select['关注度'].mean())
    city = select['城市'].iloc[0]
    address = select['街道'].iloc[0]
    count = len(select)
    age = select['房屋年限'].mode()[0]
    # response = {
    #     'data':[{'totalprice_average':averagetotalprice},{'price_average':averageprice},{'attention_average':averageattention},{'city':city},{'city':city},{'count':count},{'name':areaname}]
    # }
    response ={
        'data':[{'totalprice_average':averagetotalprice,'price_average':averageprice,'attention_average':averageattention,'city':city,'address':address,'count':count,'name':areaname,'age':age}]
    }
    return jsonify(response)

# 查询小区房屋面积分布数据
@app.route('/info/area/areasection',methods=['get'])
def areasection():
    print('查询小区房屋面积分布数据')
    data = pd.read_csv('../data/deal/total_fordraw.csv', index_col=0)
    areaname = request.args.get('area', '', type=str)
    # areaname = '万泰城章'
    select = data[data['小区名称'] == areaname]
    max = int(select['建筑面积'].max()) + 1
    min = int(select['建筑面积'].min())
    bins = np.linspace(min, max, 6)
    select['面积区间'] = pd.cut(select['建筑面积'], bins)
    count = pd.DataFrame(select['面积区间'].value_counts().sort_index())['count'].tolist()
    label = []
    for i in range(0, 5):
        label.append(str(bins.tolist()[i]) + '-' + str(bins.tolist()[i + 1]) + 'm²')
    responses = {
        'data':[{'label':label,'count':count}]
    }
    return jsonify(responses)

# 查询小区房屋装修情况
@app.route('/info/area/decorate',methods=['get'])
def decorate():
    print('查询小区房屋装修情况')
    data = pd.read_csv('../data/deal/total_fordraw.csv', index_col=0)
    areaname = request.args.get('area', '', type=str)
    select = data[data['小区名称'] == areaname]
    count = select['装修情况'].value_counts().values.tolist()
    label = ['精装', '简装', '毛坯']
    responses = {
        'data':[{'label':label,'count':count}]
    }
    return jsonify(responses)

# 查询小区房屋楼层信息
@app.route('/info/area/floor',methods=['get'])
def floor():
    print('查询小区楼层信息')
    data = pd.read_csv('../data/deal/total_fordraw.csv', index_col=0)
    areaname = request.args.get('area', '', type=str)
    select = data[data['小区名称'] == areaname]
    count = select['所在楼层'].value_counts().tolist()
    label = ['低(10楼以下)', '中(10-20楼)', '高(20楼以上)']
    responses = {
        'data':[{'label':label,'count':count}]
    }
    return jsonify(responses)

# 查询小区房屋单价分布信息
@app.route('/info/area/price',methods=['get'])
def price():
    print('查询小区房屋单价分布信息')
    data = pd.read_csv('../data/deal/total_fordraw.csv', index_col=0)
    areaname = request.args.get('area', '', type=str)
    select = data[data['小区名称'] == areaname]
    max = select['单价'].max() + 1
    min = select['单价'].min() - 1
    bins = np.linspace(min, max, 6)
    select['单价区间'] = pd.cut(select['单价'], bins)
    count = pd.DataFrame(select['单价区间'].value_counts().sort_index())['count'].tolist()
    label = []
    for i in range(0, 5):
        label.append(str(bins.tolist()[i]) + '-' + str(bins.tolist()[i + 1]) + '元/m²')
    responses = {
        'data': [{'label': label, 'count': count}]
    }
    return jsonify(responses)

# 查询小区房屋交易记录
@app.route('/info/area/history',methods=['get'])
def history():
    print('查询小区历史交易数据')
    data = pd.read_csv('../data/deal/total_forhistory.csv', index_col=0)
    areaname = request.args.get('area', '', type=str)
    # areaname = '万泰城章'
    select = data[data['小区名称'] == areaname]
    select['单价'] = select['单价'].astype(float)
    select['关注度'] = select['关注度'].astype(float)
    length = len(select)
    record = []
    name = ['column1', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7', 'column8', 'column9',
            'column10', 'column11', 'column12', 'column13', 'column14', 'column15', 'column16', 'column17', 'column18',
            'column19']
    for i in range(1, length):
        dict = {}
        row = select.iloc[i].tolist()
        for i in range(len(row)):
            dict[name[i]] = row[i]
        record.append(dict)

    responses = {
        'data':[{'data':record}]
    }
    return jsonify(responses)

# 用户注册的接口
@app.route('/index/register',methods=['get'])
def register():
    print('用户注册')
    data = pd.read_csv('../data/deal/user.csv',index_col=0)
    username = request.args.get('username', '', type=str)
    password = request.args.get('password','',type=str)
    # 默认头像地址
    avatar = 'https://tse3-mm.cn.bing.net/th/id/OIP-C.YNWUhXfbevWgFsAdLuTt2AHaHa?w=210&h=211&c=7&r=0&o=5&pid=1.7'
    newrow = {'username':username,'password':password,'avatar':avatar}
    judge = ''
    # 如果该该用户名不存在于文件中则进行写入
    if (data[data['username']==username].empty):
        data = data._append(newrow,ignore_index=True)
        data.to_csv('../data/deal/user.csv')
        judge = 'succeed'
    # 如果该用户存在于文件中则拒绝进行二次注册
    else:
        judge = 'fail'
    responses = {
        'data':[{'result':judge}]
    }
    return jsonify(responses)

# 用户登录的接口
@app.route('/index/login',methods=['get'])
def login():
    print('用户登录验证')
    data = pd.read_csv('../data/deal/user.csv',index_col=0)
    username = request.args.get('username', '', type=str)
    password = request.args.get('password', '', type=str)
    avatar = ''
    judge = ''
    token = ''
    if (data[data['username']==username].empty==False and str(data[data['username']==username]['password'].iloc[0])==password):
        judge = 'succeed'
        letters = string.ascii_uppercase
        token = ''.join(random.choices(letters, k=24))
        avatar = data[data['username'] == username]['avatar'].iloc[0]
    else:
        judge = 'fail'
    responses = {
        'data':[{'result':judge,'token':token,'avatar':avatar}]
    }
    return jsonify(responses)

# 修改用户头像信息
@app.route('/index/avatar',methods=['get'])
def avatar():
    print('修改用户头像信息')
    data = pd.read_csv('../data/deal/user.csv',index_col=0)
    username = request.args.get('username', '', type=str)
    newavatar = request.args.get('avatar','',type=str)
    print(newavatar)
    #　修改头像信息
    data.loc[data['username'] == username ,'avatar'] = newavatar
    # 重新写入到文件中
    data.to_csv('../data/deal/user.csv')
    responses = {
        'data':[{'result':'succeed'}]
    }
    return jsonify(responses)

# 房价预测接口
@app.route('/index/perdict',methods=['get'])
def predict():
    print('房价预测')
    xiaoquming = request.args.get('xiaoquming','',type=str)
    louceng =  request.args.get('louceng',None,int)
    mianji = request.args.get('mianji',None,type=float)
    huxing = request.args.get('huxing','',type=str)
    jianzhuleixing = request.args.get('jianzhuleixing','',type=str)
    chaoxiang =request.args.get('chaoxiang','',type=str)
    jianzhujiegou = request.args.get('jianzhujiegou','',type=str)
    zhuangxiu = request.args.get('zhuangxiu','',type=str)
    dianti = request.args.get('dianti','',type=str)
    jiaoyiquanshu = request.args.get('jiaoyiquanshu','',type=str)
    yongtu = request.args.get('yongtu','',type=str)
    age = request.args.get('age',None,type=int)
    chanquan = request.args.get('chanquan','',type=str)
    city = request.args.get('city','',type=str)
    bedroom = request.args.get('bedroom',None,type=int)
    keting = request.args.get('keting',None,type=int)
    chufang = request.args.get('chufang',None,type=int)
    cesuo = request.args.get('cesuo',None,type=int)
    newdata = [xiaoquming, louceng, mianji, huxing, jianzhuleixing, chaoxiang, jianzhujiegou, zhuangxiu, dianti,
               jiaoyiquanshu, yongtu, age, chanquan, city, bedroom, keting, chufang, cesuo]
    print(newdata)
    # 读取数据集
    data = pd.read_csv('../data/deal/data.csv', index_col=0)
    # 将新的行追加到末尾
    newRow = pd.DataFrame([newdata], columns=data.columns)
    data = pd.concat([data, newRow], ignore_index=True)

    # 处理object类型的特征列
    # 户型结构编码
    def houseTypeStructure(s):
        if s == '平层':
            return 0
        elif s == '跃层':
            return 1
        elif s == '错层':
            return 2
        elif s == '复式':
            return 3
        elif s == 'Loft':
            return 4

    # 建筑类型编码
    def buildingType(s):
        if s == '板楼':
            return 0
        elif s == '板塔结合':
            return 1
        elif s == '塔楼':
            return 2
        elif s == '平房':
            return 3

    # 　建筑结构编码
    def buildingStructure(s):
        if s == '钢混结构':
            return 0
        elif s == '砖混结构':
            return 1
        elif s == '混合结构':
            return 2
        elif s == '框架结构':
            return 3
        elif s == '钢结构':
            return 4
        elif s == '转木结构':
            return 5

    # 装修情况编码
    def decorateSituation(s):
        if s == '精装':
            return 0
        elif s == '简装':
            return 1
        elif s == '毛坯':
            return 2
        elif s == '其它':
            return 3

    def elevator(s):
        if s == '无':
            return 0
        elif s == '有':
            return 1

    # 房屋交易权属编码
    def tranSactionOwnnership(s):
        if s == '商品房':
            return 0
        elif s == '已购公房':
            return 1
        elif s == '回迁房':
            return 2
        elif s == '私产':
            return 3

    # 房屋用途编码
    def usageOfHouse(s):
        if s == '普通住宅':
            return 0
        elif s == '商住两用':
            return 1
        elif s == '别墅':
            return 2

    # 产权所属编码
    def ownership(s):
        if s == '共有':
            return 0
        elif s == '非共有':
            return 1

    # 城市编码
    def city(s):
        if s == '拱墅':
            return 0
        elif s == '临平区':
            return 1
        elif s == '钱塘区':
            return 2
        elif s == '萧山':
            return 3
        elif s == '西湖':
            return 4
        elif s == '余杭':
            return 5
        elif s == '滨江':
            return 6
        elif s == '临安':
            return 7
        elif s == '上城':
            return 8
        elif s == '富阳':
            return 9

    data['户型结构'] = data['户型结构'].apply(houseTypeStructure)
    data['建筑类型'] = data['建筑类型'].apply(buildingType)
    data['建筑结构'] = data['建筑结构'].apply(buildingStructure)
    data['装修情况'] = data['装修情况'].apply(decorateSituation)
    data['配备电梯'] = data['配备电梯'].apply(elevator)
    data['交易权属'] = data['交易权属'].apply(tranSactionOwnnership)
    data['房屋用途'] = data['房屋用途'].apply(usageOfHouse)
    data['产权所属'] = data['产权所属'].apply(ownership)
    data['城市'] = data['城市'].apply(city)

    # 独热编码(哑变量处理)
    def chaoxiang(df):
        chaoxiangColumns = ['南', '南 北', '东南', '北', '东', '西', '西南', '东 南 北', '东 南', '东南 南', '南 西 北', '西北']
        if df['房屋朝向'] not in chaoxiangColumns:
            return "其他朝向"
        else:
            return df['房屋朝向']

    data['房屋朝向'] = data.apply(lambda x: chaoxiang(x), axis=1)
    one_hot_col_names = ['小区名称', '房屋朝向']
    data_onehot = pd.get_dummies(data[one_hot_col_names])
    data = pd.concat([data, data_onehot], axis=1)

    # 按小区和城市连接平局关注度和单价
    average_attention_area = pd.read_csv('../data/deal/average_attention_area.csv', index_col=0)
    result = pd.merge(data, average_attention_area, on='小区名称', how='left')
    average_price_area = pd.read_csv('../data/deal/average_price_area.csv', index_col=0)
    result = pd.merge(result, average_price_area, on='小区名称', how='left')
    average_price_city = pd.read_csv('../data/deal/average_price_city.csv', index_col=0)
    result = pd.merge(result, average_price_city, on='城市', how='left')

    # 删除不必要字段
    result.drop(columns=['小区名称','房屋朝向'],inplace=True)

    # 提取出待预测数据
    waitPredict = result.tail(1)

    # 加载模型
    model_xgb = pickle.load(open('../data/model/xgboost.pkl', 'rb'))
    model_rf = pickle.load(open('../data/model/randomForest.pkl','rb'))
    predict_xgb = model_xgb.predict(waitPredict)
    predict_rf = model_rf.predict(waitPredict)
    price_xgb = predict_xgb[0]
    predict_rf = predict_rf[0]
    price = (30.08/(30.08+29.41))*price_xgb+(29.41/(30.08+29.41))*predict_rf
    price = round(price,2)
    print(price)

    responses = {
        'data': [{'result': price}]
    }

    return jsonify(responses)

if __name__ == '__main__':
    app.run(debug=True,port=8444)