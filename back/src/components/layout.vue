<template>
  <div class="layout">
    <div class="header">
      <mu-appbar>
        <div class="logo">
          猫阅读后台管理系统 v1.0
        </div>
        <mu-icon-button icon="person" slot="right" to="userManage"/>
      </mu-appbar>
    </div>
    <div class="content">
      <div class="content-left">
        <mu-list @change="handleListChange" :value="activeList">

          <mu-list-item title="书籍管理" toggleNested value="list1">
            <mu-icon slot="left" value="book"/>
            <mu-list-item slot="nested" title="上传书籍" value="list11" to="bookUpload">
              <mu-icon slot="left" value="file_upload"/>
            </mu-list-item>
            <mu-list-item slot="nested" title="书籍列表" value="list12" to="bookList">
              <mu-icon slot="left" value="chrome_reader_mode"/>
            </mu-list-item>
          </mu-list-item>

          <mu-list-item title="界面管理" toggleNested value="list2">
            <mu-icon slot="left" value="domain"/>
            <mu-list-item slot="nested" title="推荐管理" value="list21">
              <mu-icon slot="left" value="pan_tool"/>
            </mu-list-item>
            <mu-list-item slot="nested" title="排行管理" value="list22">
              <mu-icon slot="left" value="grade"/>
            </mu-list-item>
          </mu-list-item>

          <mu-list-item title="订单管理" toggleNested value="list3">
            <mu-icon slot="left" value="shopping"/>
            <mu-list-item slot="nested" title="订单数据" value="list31">
              <mu-icon slot="left" value="content_paste"/>
            </mu-list-item>
            <mu-list-item slot="nested" title="礼物管理" value="list32">
              <mu-icon slot="left" value="cake"/>
            </mu-list-item>
          </mu-list-item>

          <mu-list-item title="用户管理" toggleNested value="list4">
            <mu-icon slot="left" value="people"/>
            <mu-list-item slot="nested" title="普通用户" value="list41" to="userNormal">
              <mu-icon slot="left" value="perm_identity"/>
            </mu-list-item>
            <mu-list-item slot="nested" title="管理员" value="list42" to="userManage">
              <mu-icon slot="left" value="person"/>
            </mu-list-item>
          </mu-list-item>

          <mu-list-item title="数据统计" toggleNested value="list5">
            <mu-icon slot="left" value="apps"/>
            <mu-list-item slot="nested" title="用户数据" value="list51">
              <mu-icon slot="left" value="face"/>
            </mu-list-item>
            <mu-list-item slot="nested" title="网站数据" value="list52">
              <mu-icon slot="left" value="book"/>
            </mu-list-item>
          </mu-list-item>
        </mu-list>
      </div>
      <div class="content-right">
        <router-view></router-view>
      </div>
    </div>
    <mu-appbar>
      <div class="footer">
        Cat Reading Background ©2017 Created by Beluga
      </div>
    </mu-appbar>
  </div>
</template>
<script>
export default {
  data () {
    return {
      activeTab: 'tab1',
      activeList: 'list1',
      breadSubTitle: "#/testBread"
    }
  },
  methods: {
    handleTabChange (val) {
      this.activeTab = val
    },
    handleListChange (val) {
      this.activeList = val
    }
  }
}
</script>
<style scoped>
.layout{
  /*height: 100%;*/
  background-color: rgb(236, 236, 236);
}

.logo{
  font-size: 24px;
  color: white;
  display: inline-block;
  padding: 10px 20px;
}

.nav{
  display: inline-block;
  width: calc(100% - 150px);
  margin: 0 auto;
}

.content{
  height: 100%;
  overflow: hidden;
}

.content-left{
  width: 20%;
  float: left;
  background-color: white;
  margin-bottom: -4000px;
  padding-bottom: 4000px;
}

.content-right{
  width: 80%;
  height: auto;
  display: inline-block;
  float: right;
  padding: 10px 20px;
  background-color: rgba(0, 0, 0, 0)
}

.body{
  background-color: white;
  border-radius: 5px;
  min-height: 500px;
}

.footer{
  color: #f3f3f3;
  font-size: 12px;
  text-align: center;
}
</style>
