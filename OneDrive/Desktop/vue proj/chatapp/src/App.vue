<template>
  <div id="app" class="app">
    <div class="container">
      <div class="sidebar">
        <company-list :companies="companies" @selectUser="selectUser" @addUser="addUserToCompany" />
      </div>
      <div class="main">
        <chat-history :selectedUser="selectedUser" v-if="selectedUser" />
      </div>
    </div>
  </div>
</template>

<script>
import CompanyList from './components/CompanyList.vue';
import ChatHistory from './components/ChatHistory.vue';

export default {
  name: 'App',
  components: {
    CompanyList,
    ChatHistory
  },
  data() {
    return {
      companies: [
        {
          name: 'Company A',
          users: [
            { id: 1, name: 'User 1', chatHistory: [] },
            { id: 2, name: 'User 2', chatHistory: [] }
          ],
          usersVisible: false,
          color: '#7289da'
        },
        {
          name: 'Company B',
          users: [
            { id: 3, name: 'User 3', chatHistory: [] },
            { id: 4, name: 'User 4', chatHistory: [] }
          ],
          usersVisible: false,
          color: '#43b581'
        }
      ],
      selectedUser: null
    };
  },
  methods: {
    selectUser(user) {
      this.selectedUser = user;
    },
    addUserToCompany(companyName, newUser) {
      const company = this.companies.find(company => company.name === companyName);
      if (company) {
        company.users.push({ id: Date.now(), name: newUser, chatHistory: [] });
      }
    }
  }
};
</script>

<style scoped>
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
  height: 90vh; /* Full screen height */
  width:90vh;
  background-color: #36393f; /* Discord background color */
  color: #dcddde; /* Discord text color */
  display: flex; /* Allow full-screen element to fill vertically */
}

.app {
  flex: 1; /* Take up the entire available space */
  display: flex;
}

.container {
  flex: 1; /* Split available space between sidebar and main content */
  display: flex;
  height: 100%; /* Inherit full height from body */
}

.sidebar {
  width: 240px; /* Fixed sidebar width */
  background-color: #4f545c; /* Discord channel list background color */
  color: #dcddde; /* Discord text color */
  border-right: 1px solid rgba(0, 0, 0, 0.1); /* Optional border */
}

.main {
  flex: 1; /* Fill remaining space */
  background-color: #40444b; /* Discord chat background color */
  color: #dcddde; /* Discord text color */
  padding: 15px; /* Add some padding for content */
}
</style>
