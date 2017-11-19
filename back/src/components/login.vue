<template>
<div class="body">
  <div class="box">
    <mu-paper class="login_card" :zDepth="1">
      <br/>
      <mu-card-title title="猫阅读后台管理系统" subTitle="本系统不支持注册，请联系猫阅读管理员。"/>
      <div class="login">
        <mu-text-field label="账号" labelFloat/><br/>
        <mu-text-field label="密码" hintText="请输入密码" type="password" labelFloat/><br/>
        <br/>
        <mu-raised-button label="登 录" class="raised-button"/>
      </div>
    </mu-paper>
  </div>
  <mu-circular-progress :size="20" color="red"/>
</div>
</template>

<style scoped>
.body{
  width: 100%;
  height: 100%;
  background-color: #bdbdbd;
  text-align: center;
}
.box{
  text-align: center;
}
.login_card{
  display: inline-block;
  height: 420px;
  width: 400px;
  margin-top: 150px;
  margin-bottom: 200px;
  text-align: center;
}
.login{
  margin: 30px;
}
.raised-button{
  height: 50px;
  width: 256px;
  background-color: #f44336;
  color: white;
  font-size: 16px;
}
</style>
