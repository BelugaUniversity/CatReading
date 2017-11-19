<template>
  <div>
    <div class="breadcrumb">
      <mu-breadcrumb>
        <mu-breadcrumb-item href="/">主页</mu-breadcrumb-item>
        <mu-breadcrumb-item :href="breadSubTitle">{{ breadSubTitle }}</mu-breadcrumb-item>
        <mu-breadcrumb-item>上传书籍</mu-breadcrumb-item>
      </mu-breadcrumb>
    </div>
  </div>
</template>
