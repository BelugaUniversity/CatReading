<template>
  <div class="layout">
    <div class="header">
     
      <div class="title"><a href="#"><i class="material-icons arrow">keyboard_arrow_left</i></a>第一章 大闹天宫</div>
    </div>
    <div class="content">
      <div class="charpterContent">
        <div>
          <div></div>
          <h4 class="charpterTitle">第一章 vue的使用文档</h4>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南熟悉 Vue本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
          <p>CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，熟悉 Vue 本身之后再研究 CLI。</p>
        </div>
        <mu-infinite-scroll :scroller="scroller" :loading="loading" @load="loadMore"/>
      </div>
      <div>
        <mu-drawer right :open="catalogOpen" @close="catalogToggle()" :docked="false" width="80%">
          <mu-appbar title="Muse UI"/>
          <mu-list>
            <mu-list-item title="Menu Item 1"/>
            <mu-list-item title="Menu Item 2"/>
            <mu-list-item title="Menu Item 3"/>
          </mu-list>
        </mu-drawer>
      </div>
    </div>
    <div class="footer">
      <mu-raised-button @click="openBottomSheet" label="Open Bottom Sheet" />
      <mu-bottom-sheet :open="bottomSheet" @close="closeBottomSheet">
        <div>
          <span class="fontReduce">调整字体大小</span>
          <mu-slider v-model="progrssVal" :step="1" class="demo-slider"/>
        </div>
        <mu-bottom-nav :value="bottomNav" @change="handleChange">
          <mu-bottom-nav-item value="catalog" title="目录" icon="format_list_bulleted"/>
          <mu-bottom-nav-item value="progrss" title="进度" icon="trending_flat"/>
          <mu-bottom-nav-item value="setting" title="设置" icon="text_format"/>
          <mu-bottom-nav-item value="day" title="日间" icon="wb_sunny"/>
          <mu-bottom-nav-item value="night" title="夜间" icon="timelapse"/>
        </mu-bottom-nav>
      </mu-bottom-sheet>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.scroller = this.$el
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      loading: false,
      scroller: null,
      bottomSheet: false,
      bottomNav: '',
      catalogOpen: false,
      progrssVal: 10
    }
  },
  methods: {
    loadMore: function(){
      //alert("加载中")
    },
    closeBottomSheet () {
      this.bottomSheet = false
    },
    openBottomSheet () {
      this.bottomSheet = true
    },
    handleChange (val) {
      this.bottomNav = val
      if(val == "catalog"){
        this.catalogOpen = true
        this.bottomSheet = false
      }
    },
    catalogToggle () {
      this.catalogOpen = !this.catalogOpen
      this.bottomNav = ''
    }
  }
}
</script>
<style>
  html{
    font-size: 16px;
  }
  .mu-item-content{
    text-align: left;
    position: absolute;
  }
  .arrow{
    float: left;
    line-height: 40px;
    padding: 0 10px;
    color: rgba(0,0,0,.4);
  }
  .title{
    width: 100%;
    height: 40px;
    
    line-height: 40px;
    background: #DDD;
    color: rgba(0,0,0,.4);
    text-align: left;
    position: fixed;
    font-size: .85em;
    top: 0; 
  }
  .content{
    background-color: #DDD;
    padding: 16px;
  }
  .charpterTitle{
    padding: 56px 0 16px 0;
    font-size: 1.4em;
    text-align: left;
  }
  p{
    text-align: left;
    text-indent: 2em;
    margin: 10px 0;

  }
  .demo-slider{
    width: 80%;
    margin: 0 auto;
    
  }
  .fontReduce{
    width: 100%;
    text-align: center;
    display: inline-block;
    font-size: 18px;
    padding-top: 20px;
  }
</style>