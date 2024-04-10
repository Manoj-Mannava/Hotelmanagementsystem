<template>
  <div class="company-list">
    <h2 class="title">Companies</h2>
    <div v-for="company in companies" :key="company.name" class="company" :style="{ backgroundColor: company.color }" @click="toggleCompany(company)">
      <h3>{{ company.name }}</h3>
      <ul v-if="company.usersVisible">
        <li v-for="user in company.users" :key="user.id" @click="selectUser(user)">
          {{ user.name }}
        </li>
      </ul>
      <button v-if="company.usersVisible" class="add-user-button" @click="addUser(company.name)">Add User</button>
    </div>
  </div>
</template>

<script>
export default {
  props: ['companies'],
  methods: {
    toggleCompany(company) {
      company.usersVisible = !company.usersVisible;
    },
    selectUser(user) {
      this.$emit('selectUser', user);
    },
    addUser(companyName) {
      const newUser = prompt('Enter user name:');
      if (newUser) {
        this.$emit('addUser', companyName, newUser);
      }
    }
  }
};
</script>

<style scoped>
.company-list {
  color: #fff;
  padding-left: 20px;
}

.title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 15px;
}

.company {
  cursor: pointer;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 10px;
  transition: background-color 0.3s ease;
  position: relative;
  display: flex; 
  align-items: center;
  justify-content: space-between; 
}

.company h3 {
  margin: 0;
  font-size: 16px;
}

.company:hover {
  filter: brightness(0.9);
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  cursor: pointer;
  padding: 8px 12px;
  border-radius: 5px;
  margin-bottom: 5px;
  transition: background-color 0.3s ease;
}

li:hover {
  background-color: #4a5abf;
}

.add-user-button {
  opacity: 0; /* Initially hidden */
  transition: opacity 0.3s ease;
  /* Removed positioning properties (handled by flexbox) */
  padding: 5px 10px;
  background-color: #7289da;
  border: none;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
}

.company:hover .add-user-button { /* Show button on hover */
  opacity: 1; /* Button becomes visible */
}
</style>
