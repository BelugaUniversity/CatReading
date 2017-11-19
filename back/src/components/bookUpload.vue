<template>
  <div>
    <div class="breadcrumb">
      <mu-breadcrumb>
        <mu-breadcrumb-item href="/">主页</mu-breadcrumb-item>
        <mu-breadcrumb-item href="/">书籍管理</mu-breadcrumb-item>
        <mu-breadcrumb-item>上传书籍</mu-breadcrumb-item>
      </mu-breadcrumb>
      </br>
    </div>
    <div class="body">
      <mu-card>
        <mu-card-title title="上传书籍" subTitle="请仔细阅读下方注意事项"/>
        <mu-card-text>
        ⚠️ 注意事项
        </br></br>
          1. 书籍上传格式为 *.txt，请不要使用其他格式。
        </br>
          2. 书籍上传过程中会根据章节名称自动切分，保证书籍中每章开头有第 x 章。
        </br>
          3. 书籍上传可以批量上传，请安装 CTRL 键依次选择书籍。
        </br>
          4. 点击下方按钮开始上传书籍。
        </mu-card-text>

        <mu-card-actions style="margin-left: 15px">
          <mu-raised-button label="上传书籍" primary/>
          <input type="file" class="inputStyle"/>
        </mu-card-actions>
        </br>

      </mu-card>
      <br/>
      <mu-card>
        <mu-card-title title="书籍列表" subTitle="此次上传后的书籍都在这里"/>
        <mu-card-text>
        ⚠️ 注意事项
        </br></br>
          1. 根据上传书籍的内容，程序会自动把文件名称作为书籍名称填入书籍信息。
        </br>
          2. 如果有书籍名称错误的地方请点击修改按钮进行修改。
        </br>
          3. 在修改界面内可以预览本书的内容，确定书籍内容。
        </br>
        </br>
        </mu-card-text>


        <mu-divider/>
        <mu-table :showCheckbox="false" ref="table" style="">
          <mu-thead>
            <mu-tr>
              <mu-th>ID</mu-th>
              <mu-th>书籍名称</mu-th>
              <mu-th>书籍章节数</mu-th>
              <mu-th>操作1</mu-th>
              <mu-th>操作2</mu-th>
            </mu-tr>
          </mu-thead>
          <mu-tbody>
            <mu-tr>
              <mu-td>1</mu-td>
              <mu-td>天女三花</mu-td>
              <mu-td>100</mu-td>
              <mu-td>
                <mu-raised-button label="修改" ref="button" @click="open"/>
                <v-dialog :dialog="this.dialog"/>
              </mu-td>
              <mu-td>
                <mu-raised-button label="删除" ref="button" @click="toggle"/>
              </mu-td>
            </mu-tr>

            <mu-tr>
              <mu-td>3</mu-td>
              <mu-td>私密马赛</mu-td>
              <mu-td>3242</mu-td>
              <mu-td>
                <mu-raised-button label="修改" ref="button" @click="toggle"/>
              </mu-td>
              <mu-td>
                <mu-raised-button label="删除" ref="button" @click="toggle"/>
              </mu-td>
            </mu-tr>
          </mu-tbody>
        </mu-table>
        <mu-divider/>
        </br>
      </mu-card>
    </div>
  </div>
</template>
<script>
import dialog from '@/components/comp/dialog'
export default{
  components:{
    "v-dialog": dialog
  }
}
</script>
<style>
.inputStyle{
  width: 88px;
  height: 36px;
  outline: medium none;
  position: absolute;
  filter: alpha(opacity=0);
  -moz-opacity: 0;
  opacity: 0;
  left: 8px;
  top: 8px;
}
</style>
