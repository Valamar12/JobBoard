<script>
  import jwt_decode from 'jwt-decode';
  
  let username = '';
  let password = '';

  async function handleLogin() {
  const response = await fetch('http://localhost:8000/api/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: username,
      password: password,
    }),
  });

  if (response.ok) {
    const data = await response.json();
    const token = data.access; 
    const decodedToken = jwt_decode(token);
    const expirationDate = new Date(decodedToken.exp * 1000);
    document.cookie = `authToken=${token}; expires=${expirationDate.toUTCString()}; path=/;`;
    alert('Login successful');
    if (decodedToken.is_superuser) {
      window.location.href = '/admin';
    }
    else {
      window.location.href = '/';
    }
  } 
  else {
    alert('Login failed');
  }
}
</script>
<head>
  <link rel="stylesheet" href="styles.css"/>
</head>
<section>
<div class="container">
<form on:submit="{handleLogin}">
  <div class = "form-field">
  <label for="username">Username:</label>
  <input type="text" id="username" bind:value={username} required />
  </div>
  <div class = "form-field">
  <label for="password">Password:</label>
  <input type="password" id="password" bind:value={password} required />
  </div>
  <div class = "form-button">
  <button type="submit" class="button">Log In</button>
  </div>
</form>
</div>
<!--<button on:click="{Disconnect}">Disconnect</button>-->
</section>
