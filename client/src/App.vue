<template>
  <form
    @submit.prevent
    @submit="upload"
  >
    <input
      type="file"
      enctype="multipart/form-data"
      @change="onFileChange"
    />
    <button type="submit">
      upload
    </button>
  </form>
</template>

<script>
import axios from 'axios'
import config from './config.js'

export default {
  data() {
    return {
      file: null,
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files;
        if (!files.length) return;
      this.file = files[0];
    },
    upload() {
      const formData = new FormData();
      formData.append('file', this.file);
      axios({
        method: "post",
        url: `http://${config.host}:${config.port}/load_torrent`,
        data: formData,
        headers: { "Content-Type": "multipart/form-data" },
      })
        .then((response) => console.log(response))
        .catch((error) => console.log(error));
    }
  },
}
</script>

<style>

</style>
