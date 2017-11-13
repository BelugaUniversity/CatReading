<template>
    <!-- <el-menu theme="light" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <div id="b-menu">
        <el-menu-item index="1">搜书</el-menu-item>
        <el-menu-item index="2">书库</el-menu-item>
        <el-menu-item index="3">登录</el-menu-item>
      </div>
    </el-menu> -->
    <div id="header">
    <img id="logo" src="../../assets/img/png/logo.png"/>
    <el-menu theme="light" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
           <el-menu-item index="1"><i class="el-icon-search"></i>搜书</el-menu-item>
           <el-menu-item index="2">书库</el-menu-item>
           <el-menu-item index="3">登录</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import Vue from 'vue'
import {Menu, MenuItem, Icon} from 'element-ui'
Vue.component(Menu.name, Menu)
Vue.component(MenuItem.name, MenuItem)
Vue.component(Icon.name, Icon)

export default {
  data () {
    return {
      activeIndex: '1'
    }
  }
}
</script>

<style scoped>
#header{
  height: 10%;
}

#logo{
  height: 80%;
  padding-left: 10px;
  float: left;
}

.el-menu-demo{
  background-color: #ffffff;
  margin-bottom: 20px;
  float: right;
}

#b-menu{
}

</style>
