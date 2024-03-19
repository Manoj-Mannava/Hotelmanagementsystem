<!-- components/ChatHistory.vue -->
<template>
  <div class="chat-history">
    <h3>Chat History for {{ selectedUser.name }}</h3>
    <div class="chat-box">
      <ul>
        <li v-for="message in selectedUser.chatHistory" :key="message.id" :class="{ 'sent': message.sentByMe, 'received': !message.sentByMe }">
          {{ message.text }}
        </li>
      </ul>
      <div class="message-input">
        <input type="text" placeholder="Type your message..." v-model="newMessage" @keyup.enter="sendMessage">
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['selectedUser'],
  data() {
    return {
      newMessage: ''
    };
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.selectedUser.chatHistory.push({ id: Date.now(), text: this.newMessage, sentByMe: true });
        this.newMessage = '';
      }
    }
  }
};
</script>

<style scoped>
.chat-history {
  flex: 1;
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.chat-history h3 {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 600;
}

.chat-box {
  height: 400px;
  overflow-y: auto;
  border-radius: 10px;
  background-color: #fff;
  padding: 15px;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  padding: 8px 12px;
  border-radius: 5px;
  margin-bottom: 5px;
  max-width: 70%;
}

.sent {
  background-color: #007bff;
  color: #fff;
  align-self: flex-end;
}

.received {
  background-color: #e5e5ea;
  color: #000;
}

.message-input {
  margin-top: 15px;
  display: flex;
  align-items: center;
}

.message-input input[type="text"] {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}

.message-input button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;   
  cursor: pointer;
}

.message-input button:hover {
  background-color: #0056b3;
}
</style>
