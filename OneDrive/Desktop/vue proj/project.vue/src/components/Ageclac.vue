<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Age Calculator</title>
  <!-- Include Vue.js library -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>

<div id="app">
  <h1>Age Calculator</h1>
  <label for="birthdate">Enter your birthdate:</label>
 <input type="date" id="birthdate" v-model="birthdate">
  <button @click="calculateAge">Calculate Age</button>
  
  <p v-if="age !== null">Your age is {{ age }} years old.</p>
  <p v-if="error">{{ error }}</p>
</div>

<script>
new Vue({
  el: '#app',
  data: {
    birthdate: null,
    age: null,
    error: null
  },
  methods: {
    calculateAge() {
      if (!this.birthdate) {
        this.error = 'Please enter your birthdate';
        return;
      }

      const today = new Date();
      const birthDate = new Date(this.birthdate);
      const diff = today.getTime() - birthDate.getTime();
      const ageDate = new Date(diff);

      this.age = Math.abs(ageDate.getUTCFullYear() - 1970);
      this.error = null;
    }
  }
});
</script>

</body>
</html>
