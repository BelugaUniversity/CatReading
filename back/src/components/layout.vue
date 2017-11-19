<template>
  <div class="layout">
    <div class="header">
      <mu-appbar>
        <div class="logo">
          猫阅读后台管理系统
        </div>
        <mu-flat-button label="个人中心" slot="right"/>
        <mu-icon-button icon="person" slot="right"/>
      </mu-appbar>
    </div>
    <div class="content">
      <div class="content-left">
        <mu-list @change="handleListChange" :value="activeList">

          <mu-list-item title="书籍管理" toggleNested value="list1">
            <mu-icon slot="left" value="book"/>
            <mu-list-item slot="nested" title="上传书籍" value="list11">
              <mu-icon slot="left" value="file_upload"/>
            </mu-list-item>
            <mu-list-item slot="nested" title="书籍列表" value="list12">
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
            <mu-list-item slot="nested" title="普通用户" value="list41">
              <mu-icon slot="left" value="perm_identity"/>
            </mu-list-item>
            <mu-list-item slot="nested" title="管理员" value="list42">
              <mu-icon slot="left" value="person"/>
            </mu-list-item>
          </mu-list-item>

          <mu-list-item title="数据统计" toggleNested value="list5">
            <mu-icon slot="left" value="apps"/>
            <mu-list-item slot="nested" title="用户数据" value="list51">
              <mu-icon slot="left" value="face"/>
            </mu-list-item>
            <mu-list-item slot="nested" title="书籍书籍" value="list52">
              <mu-icon slot="left" value="book"/>
            </mu-list-item>
          </mu-list-item>
        </mu-list>
      </div>
      <div class="content-right">
        <div class="breadcrumb">
          <mu-breadcrumb>
            <mu-breadcrumb-item href="/">主页</mu-breadcrumb-item>
            <mu-breadcrumb-item href="/">书籍管理</mu-breadcrumb-item>
            <mu-breadcrumb-item>上传书籍</mu-breadcrumb-item>
          </mu-breadcrumb>
        </div>
        <div class="body">
          <mu-card>
            <mu-card-title title="上传书籍" subTitle="@ToDo"/>
            <mu-card-text>
              散落在指尖的阳光，我试着轻轻抓住光影的踪迹，它却在眉宇间投下一片淡淡的阴影。
              调皮的阳光掀动了四月的心帘，温暖如约的歌声渐起。
              似乎在诉说着，我也可以在漆黑的角落里，找到阴影背后的阳光，
              找到阳光与阴影奏出和谐的旋律。我要用一颗敏感赤诚的心迎接每一缕滑过指尖的阳光！
            </mu-card-text>

            <mu-raised-button label="上传书籍" primary/>

          </mu-card>
          <br/>
          <mu-card>
            <mu-card-title title="Content Title" subTitle="Content Title"/>
            <mu-card-text>
              散落在指尖的阳光，我试着轻轻抓住光影的踪迹，它却在眉宇间投下一片淡淡的阴影。
              调皮的阳光掀动了四月的心帘，温暖如约的歌声渐起。
              似乎在诉说着，我也可以在漆黑的角落里，找到阴影背后的阳光，
              找到阳光与阴影奏出和谐的旋律。我要用一颗敏感赤诚的心迎接每一缕滑过指尖的阳光！
            </mu-card-text>
            <mu-card-actions>
              <mu-flat-button label="Action 1"/>
              <mu-flat-button label="Action 2"/>
            </mu-card-actions>
          </mu-card>
          <br/>
          <mu-card>
            <mu-raised-button label="unselect" @click="unselect"/>
            <mu-table multiSelectable enableSelectAll ref="table">
              <mu-thead>
                <mu-tr>
                  <mu-th>ID</mu-th>
                  <mu-th>Name</mu-th>
                  <mu-th>Status</mu-th>
                </mu-tr>
              </mu-thead>
              <mu-tbody>
                <mu-tr>
                  <mu-td>1</mu-td>
                  <mu-td>John Smith</mu-td>
                  <mu-td>Employed</mu-td>
                </mu-tr>
                <mu-tr>
                  <mu-td>2</mu-td>
                  <mu-td>Randal White</mu-td>
                  <mu-td>Unemployed</mu-td>
                </mu-tr>
                <mu-tr>
                  <mu-td>3</mu-td>
                  <mu-td>Stephanie Sanders</mu-td>
                  <mu-td>Employed</mu-td>
                </mu-tr>
                <mu-tr>
                  <mu-td>4</mu-td>
                  <mu-td>Steve Brown</mu-td>
                  <mu-td>Employed</mu-td>
                </mu-tr>
              </mu-tbody>
            </mu-table>
          </mu-card>

        </div>
      </div>
    </div>
    <div class="footer">
      Cat Reading Background ©2017 Created by Beluga
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      activeTab: 'tab1',
      activeList: 'list1'
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
  height: 100%;
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
  display: inline-block;
  float: right;
  padding: 10px 20px;
  background-color: rgba(0, 0, 0, 0)
}

.breadcrumb{
  margin: 8px 0;
}

.body{
  background-color: white;
  border-radius: 5px;
  min-height: 500px;
}

.footer{
  padding: 20px 0;
  text-align: center;
}
</style>
