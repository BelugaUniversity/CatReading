<template>
  <div>
    <mu-dialog :open="oDialog" title="书籍编辑：" @close="close">
    <div class="dialog">
      <mu-flexbox>
        <mu-flexbox-item>
          书名
        </mu-flexbox-item>
        <mu-flexbox-item>
          <mu-text-field v-model="value"/>
        </mu-flexbox-item>
      </mu-flexbox>

      <mu-flexbox>
        <mu-flexbox-item>
          作者
        </mu-flexbox-item>
        <mu-flexbox-item>
          <mu-text-field v-model="value"/><br/>
        </mu-flexbox-item>
      </mu-flexbox>

      <mu-flexbox>
        <mu-flexbox-item>
          简介
        </mu-flexbox-item>
        <mu-flexbox-item>
          <mu-text-field hintText="多行文本输入，默认 3行，最大6行" multiLine :rows="3" :rowsMax="6"/>
        </mu-flexbox-item>
      </mu-flexbox>

      <mu-flexbox>
        <mu-flexbox-item>
          预览
        </mu-flexbox-item>
        <mu-flexbox-item>
          <mu-text-field hintText="那是一个月黑风高的夜晚，小明和小花..." disabled multiLine :rows="3" :rowsMax="6"/>
        </mu-flexbox-item>
      </mu-flexbox>
    </div>

    <mu-flat-button slot="actions" @click="close" label="取消"/>
    <mu-raised-button slot="actions" @click="close" primary label="确定"/>

    </mu-dialog>
  </div>
</template>
<script>
export default{
  data(){
    return{
      oDialog: this.dialog,
      value: "帝都三巨头"
    }
  },
  methods: {
    open () {
      this.dialog = true
    },
    close () {
      this.dialog = false
    }
  },
  props: ["dialog"]
}
</script>
<style>
.dialog{
  margin-left: 30px;
}
</style>
