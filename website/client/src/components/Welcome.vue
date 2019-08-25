<template>
    <v-container fluid fill-height class="welcome" style="max-height: 100vh;">
        <v-layout justify-center align-center column pa-5>
            <div id="content" class="display-3 font-weight-black white--text text-xs-center mb-3">AQUARIUM MANAGEMENT SYSTEM</div>
            <div id="content" class="display-1 font-weight-bold white--text text-xs-center">The all-in-one solution for remote aquarium management.</div>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    name: 'Welcome'
};
</script>

<style scoped>
.welcome {
    background: url('../assets/koi-background.jpg');
    background-size: cover;
    width: 100%;
    height: 100%;
}
#content {
    text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
}
</style>