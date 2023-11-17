<script>
import { onMount } from 'svelte';
import jwt_decode from 'jwt-decode';

   let username = '';
   let admin = '';

   onMount(async() => {
    function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
    const authToken = getCookie('authToken');
    const decodedToken = jwt_decode(authToken);
    username = decodedToken.name;
    admin = decodedToken.is_superuser;
    });

    function disconnect() {
     document.cookie = 'authToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
     window.location.href = '/connection';
}

</script>
<head>
<link rel="stylesheet" href="./styles.css"/>
</head>

<header>
	<h1><a href="http://localhost:5173">JOB BOARD</a></h1>
	<nav>
    {#if username && !admin}
    <span>Welcome {username}</span>
    <button class="button" on:click="{disconnect}">Disconnect</button>
    <a href=/account><button class="button">Account Settings</button></a>
    {:else if username && admin} 
    <span>Welcome {username}</span>
    <button class="button" on:click="{disconnect}">Disconnect</button>
    <a href=/account><button class="button">Account Settings</button></a>
    <a href=/admin><button class="button">Admin</button></a>
    {:else}
    <div class="navbtn">
		  <div><a href="http://localhost:5173/connection"><button class="button">Log In</button></a></div>
	    <div><a href="http://localhost:5173/account"><button class="button">Sign in</button></a></div>
    </div>
      {/if}	
    </nav>
</header>


