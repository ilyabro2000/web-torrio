<template>
  <form
    @submit.prevent
    @submit="onFileSubmit"
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
    onFileSubmit() {
      axios.post(`http://${config.host}:${config.port}/load_torrent`, { file: this.file });
    }
  },
}
</script>

<style>

</style>
