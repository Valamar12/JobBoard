<script>
  import jwt_decode from 'jwt-decode';

  // @ts-ignore
  let username = '';
  let password = '';
  let first_name = '';
  let last_name = '';

  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

  const AuthToken = getCookie('authToken');

  async function createUser() {
    if (AuthToken) {
      try {
        const decode = jwt_decode(AuthToken);
        const id = decode.ID;
        const response = await fetch('http://localhost:8000/api/users/update/' + id, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password, first_name, last_name }),
        });

        if (response.ok) {  
          alert("Account sucessfully updated"); 
        } else {
          alert("Error"); 
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }
    else {
      try {
        const response = await fetch('http://localhost:8000/api/users/create', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password, first_name, last_name }),
        });

        if (response.ok) {  
          alert("Account sucessfully created"); 
        } else {
          alert("Error"); 
        }
      } catch (error) {
        console.error('Error:', error);
      }
}
}

</script>
<head>
  <link rel="stylesheet" href="styles.css"/>
</head>

<section>
  <div class="container">
<form on:submit="{createUser}">

  <div class="form-field">
  <label for="first_name">First name:</label>
  <input type="text" id="first_name" bind:value={first_name}/>
  </div>

  <div class="form-field">
  <label for="last_name">Last name:</label>
  <input type="text" id="last_name" bind:value={last_name}/>
  </div>

  <div class="form-field">
  <label for="username">Username:</label>
  <input type="text" id="username" bind:value={username} required/>
   </div>

  <div class="form-field">
  <label for="password">Password:</label>
  <input type="password" id="password" bind:value={password} required/>
 </div>

   <div class="form-button">
    {#if AuthToken}
    <button type="submit" class="button">Update Account</button>
    {:else}
    <button type="submit" class="button">Create Account</button>
    {/if}
</form>
</div>

</section>
    
