<template>
    <el-row>
      <el-col :span="12" :offset="6">
        <img id="people" src="../assets/img/gif/boy-walk.gif">
        <el-input　placeholder="小蜗：开始搜索你想要的图书吧～"　icon="search"　v-model="input2"　:on-icon-click="handleIconClick">
        </el-input>
      </el-col>
    </el-row>
</template>

<script>
import Vue from 'vue'
import { Input, Row, Col } from 'element-ui'
Vue.component(Input.name, Input)
Vue.component(Row.name, Row)
Vue.component(Col.name, Col)

export default {
  name: 'search'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-weight: normal;
}

#people{
  margin-top: 100px;
  width: 30%;
  height: auto;
}
</style>
