use housedata;
CREATE TABLE historyData (
    uid VARCHAR(255) NOT NULL, -- 主键字段，不允许为空
    小区名称 VARCHAR(255),
    总价 VARCHAR(255),
    单价 VARCHAR(255),
    关注度 VARCHAR(255),
    所在楼层 VARCHAR(255),
    建筑面积 VARCHAR(255),
    户型结构 VARCHAR(255),
    建筑类型 VARCHAR(255),
    房屋朝向 VARCHAR(255),
    建筑结构 VARCHAR(255),
    装修情况 VARCHAR(255),
    配备电梯 VARCHAR(255),
    交易权属 VARCHAR(255),
    房屋用途 VARCHAR(255),
    房屋年限 VARCHAR(255),
    产权所属 VARCHAR(255),
    抵押信息 VARCHAR(255),
    所在城市 VARCHAR(255),
    所在街道 VARCHAR(255),
    PRIMARY KEY (uid) -- 设置uid为主键
);
-- 创建小区信息表 (CommunityInfo)
CREATE TABLE CommunityInfo (
    AreaId CHAR(36) PRIMARY KEY,  -- 假设AreaId是UUID形式的字符串，长度为36
    AreaName VARCHAR(255) NOT NULL,
    AveragePrice INT NOT NULL,
    AverageAttention INT NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL
);

-- 创建用户信息表 (UserInfo)
CREATE TABLE UserInfo (
    UserID CHAR(36) PRIMARY KEY,  -- 假设UserID是UUID形式的字符串，长度为36
    UserName VARCHAR(100) NOT NULL,
    PassWord VARCHAR(255) NOT NULL  -- 应该存储密码哈希值而不是明文
);

-- 创建交易记录表 (TransactionRecord)
CREATE TABLE TransactionRecord (
    ID CHAR(36) PRIMARY KEY,  -- 假设ID是UUID形式的字符串，长度为36
    AreaId CHAR(36) NOT NULL,
    Floor INT NOT NULL,
    Area FLOAT NOT NULL,
    HouseTypeStructure VARCHAR(100) NOT NULL,
    BuildingType VARCHAR(100) NOT NULL,
    Orientation VARCHAR(50) NOT NULL,
    BuildingStructure VARCHAR(100) NOT NULL,
    Decoration VARCHAR(100) NOT NULL,
    Elevator VARCHAR(50) NOT NULL,
    TransactionOwnership VARCHAR(100) NOT NULL,
    UsageOfHouse VARCHAR(100) NOT NULL,
    Ownership VARCHAR(100) NOT NULL,
    HouseType VARCHAR(100) NOT NULL,
    FOREIGN KEY (AreaId) REFERENCES CommunityInfo(AreaId)  -- 设置外键
);

ALTER TABLE CommunityInfo MODIFY AreaId INT AUTO_INCREMENT;
ALTER TABLE UserInfo MODIFY UserID INT AUTO_INCREMENT;
ALTER TABLE TransactionRecord MODIFY ID INT AUTO_INCREMENT;