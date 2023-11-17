
<script>
	// @ts-nocheck
    import AdvertCard from './AdvertCard.svelte';
	import Header from './Header.svelte';
	import FormComponent from './FormComponent.svelte';
    import { onMount } from 'svelte';
    import jwt_decode from 'jwt-decode';

	let data = [];

	onMount(async () => {
		function getCookie(name) {
         const value = `; ${document.cookie}`;
         const parts = value.split(`; ${name}=`);
         if (parts.length === 2) return parts.pop().split(';').shift();
       }
		const response = await fetch('http://localhost:8000/api/adverts');
		const jsonData = await response.json();
		data = jsonData;
		getCookie('authToken');

	});

</script>


<svelte:head>
	<title>Job Board</title>
	<meta name="description" content="Svelte demo app"/>
	<link rel="stylesheet" href="styles.css"/>
</svelte:head>

<section>
	<div class="advert-container">
	{#each data as advert (advert.id)}
		<AdvertCard {advert}/>
	{/each}
	</div>
</section>
