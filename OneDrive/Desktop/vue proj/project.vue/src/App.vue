<script setup>
import { ref } from 'vue';

const birthdate = ref(null);
const age = ref(null);
const error = ref(null);

function calculateAge() {
  if (!birthdate.value) {
    error.value = 'Please enter your birthdate';
    return;
  }

  const today = new Date();
  const birthDate = new Date(birthdate.value);
  const diff = today.getTime() - birthDate.getTime();
  const ageDate = new Date(diff);

  age.value = Math.abs(ageDate.getUTCFullYear() - 1970);
  error.value = null;
}
</script>

<template>
  <div>
    <label for="birthdate">Enter your birthdate:</label><br></br><br></br>
    <input type="date" id="birthdate" v-model="birthdate"><br></br><br></br>
    <button @click="calculateAge">Calculate Age</button>
  
    <p v-if="age !== null">Your age is {{ age }} years old.</p>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<style scoped>
/* Add your styling here */
</style>
