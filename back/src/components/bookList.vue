<template>
  <div>
  <div class="breadcrumb">
    <mu-breadcrumb>
      <mu-breadcrumb-item href="/">主页</mu-breadcrumb-item>
      <mu-breadcrumb-item href="/">书籍管理</mu-breadcrumb-item>
      <mu-breadcrumb-item>书籍列表</mu-breadcrumb-item>
    </mu-breadcrumb>
  </div>
  <div class="body">
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
</template>
