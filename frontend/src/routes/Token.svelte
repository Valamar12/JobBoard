<script>
    import jwt_decode from 'jwt-decode';
  
    const token = localStorage.getItem('token');
    if (token) {
      const decodedToken = jwt_decode(token);
      const currentTime = Math.floor(Date.now() / 1000);
  
      if (decodedToken.exp < currentTime) {
        // Token has expired, redirect to connection page
        window.location.href = '/connection';
      }
    }
</script>