<template>
  <div class="form-wrapper">
    <form
      @submit.prevent
      @submit="upload"
    >
      <input
        type="file"
        enctype="multipart/form-data"
        @change="onFileChange"
        id="input__file"
        class="input__file-button"
      />
      <label for="input__file">
        <p>Open torrent file</p>
      </label>
      <button type="submit" class="input__file-button">
        upload
      </button>
    </form>
  </div>
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
  created() {
    const socket = new WebSocket(`ws://${config.host}:${config.port}/ws`);
    socket.onopen = function(e) {
      console.log('opened', e);
    };
    socket.onerror = function(error) {
      console.log(`error: ${error.message}`);
    };
    socket.onmessage = function(event) {
      console.log(event.data);
    };
  },
}
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Lato");
* {
    margin: 0;
    padding: 0;
    font-family: Lato, Arial; 
    box-sizing: border-box;
}

.form-wrapper {
  width: 300px;
  margin: 0 auto;
}

form {
  display: flex;
  width: 100%;
  margin: 15px 0;
  text-align: center;
}

input {
  opacity: 0;
  position: absolute;
  cursor: pointer;
}

label {
  width: 100%;
  max-width: 290px;
  height: 35px;
  background: #1bbc9b;
  color: #fff;
  font-size: 1.125rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

p {
  line-height: 1;
  margin-top: 1px;
}

button {
  width: 40px;
  background: #1bbc9b;
  color: #fff;
  border: none;
  cursor: pointer;
}

</style>
