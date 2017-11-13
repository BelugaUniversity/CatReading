<template>
    <div id="footer">
      <el-row>
        <el-col :span="12" :offset="6">
          <span>ShareBOOK ©2016 Created by CC</span>
        </el-col>
      </el-row>
    </div>
</template>

<script>
import Vue from 'vue'
import { Row, Col } from 'element-ui'
Vue.component(Row.name, Row)
Vue.component(Col.name, Col)

export default {
  name: 'footer'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#footer{
  position: fixed;
  font-size: 12px;
  bottom: 10px;
  width: 100%;
  text-align: center;
  color: #48d1cc;
}
</style>
