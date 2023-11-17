<script>
	import jwt_decode from 'jwt-decode';
	import { onMount } from 'svelte';

	export let advert;
	let cardUpdate = false;
	let formUpdate = false;
	const authToken  = getCookie('authToken');
  
	function UpdateCard() {
		if (cardUpdate == true){
			cardUpdate = false;
		}
		else {
			cardUpdate = true
		}
	}

	function UpdateForm() {
		if (formUpdate == true){
			formUpdate = false;
		}
		else {
			formUpdate = true
			cardUpdate = true
		}
	}

	let status = "";
	let name = "";
  	let address = "";
	let description = "";
	let url = "";


	function getCookie(name) {
		const value = `; ${document.cookie}`;
		const parts = value.split(`; ${name}=`);
		if (parts.length === 2) return parts.pop().split(';').shift();
    }


	async function submitForm() {

		const authToken  = getCookie('authToken');
		let data;

		if (authToken) {
			console.log("user found")
			let decode = jwt_decode(authToken);
			console.log(decode)
			data = { "status": "Sent", "advert": advert.id, "user": decode.ID };
		} else {
			console.log("user not found")
			data = { "status": "Sent", "advert": advert.id, "user": 1 };
		}

		const response = await fetch("http://localhost:8000/api/application/create", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data)
		});

		if (response.ok) {
			console.log("Data sent and saved to the database.");
			alert("Application sent");
		} else {
			console.error("Failed to send data to the server.");
		}
	}

</script>

<head>
	<link rel="stylesheet" href="./styles.css"/>
</head>
<article class="advert-card">
	<h2>
		<div>{advert.title}</div>
		<div>{advert.company.name}</div>
	</h2>
    {#if !cardUpdate && !formUpdate}
		<div class="buttons">
			<div class="button" on:click="{UpdateCard}">Learn More</div>
			<div class="button" on:click="{UpdateForm}">Apply</div>
		</div>
	{/if}

    {#if cardUpdate && !formUpdate}
		<div><h2>{advert.description}</h2></div>
		<div><h2>{advert.salary}€</h2></div>
		<div><h2>{advert.company.address}</h2></div>
		<div><h2>{advert.id}</h2></div>
		<div class="buttons">
			<div role="button" tabindex="0" class="button" on:click="{UpdateCard}">See less</div>
			<div role="button" tabindex="0"class="button" on:click="{UpdateForm}">Apply</div>
		</div>
	{/if}

    {#if !cardUpdate && formUpdate || cardUpdate && formUpdate}
		<div><h2>{advert.description}</h2></div>
		<div><h2>{advert.salary}€</h2></div>
		<div><h2>{advert.company.address}</h2></div>
		<div><h2>{advert.id}</h2></div>

		<form on:submit class="FormComponent">
			<div class="input-field">
				<label for="first_name">First Name</label>
				<input type="text" id="first_name" bind:value={name}/>
			</div>

			<div class="input-field">
				<label for="last_name">Last Name</label>
				<input type="text" id="last_name" bind:value={address}/>
			</div>
			
			<div class="input-field">
				<label for="email">Email</label>
				<input type="email" id="email" bind:value={description}/>
			</div>
			
			<div class="input-field">
				<label for="message">MOTIVATION</label>
				<textarea id="message" bind:value={url}></textarea>
			</div>
			
			<div class="form-buttons">
				<div class="button" on:click="{UpdateCard}" on:click="{UpdateForm}">See less</div>
				<div class="button" on:click="{submitForm(advert)}">Submit</div>
			</div>
		</form>
	{/if}

</article>

<!-- <article class="advert-card">
	<h2>

		<div>|{advert.title}</div>
		<div>|{advert.company.name}</div>
		<div>|{advert.description}</div>
		<div>|{advert.salary}€</div>
		<div>|{advert.company.address}</div>
		<div>|{advert.id}</div>
		<slot name="title">
			<span class="missing">Unknown name</span>
		</slot>

		<slot name="description">
			<span class="missing">Unknown description</span>
		</slot>
	</h2>
    {#if !cardUpdate && !formUpdate}
		<div class="buttons">
			<div class="button" on:click="{UpdateCard}">Learn More</div>
			<div class="button" on:click="{UpdateForm}">Apply</div>
		</div>
	{/if}

    {#if cardUpdate && !formUpdate}

	<div class="fulldesc">
		<slot name="fulldesc">
			<span class="missing">Unknown description</span>
		</slot>
	</div>

	<div class="wages">
		<slot name="wages">
			<span class="missing">Unknown description</span>
		</slot>
	</div>

	<div class="place">
		<slot name="place">
			<span class="missing">Unknown description</span>
		</slot>
	</div>

	<div class="buttons">
		<div class="button" on:click="{UpdateCard}">See less</div>
		<div class="button" on:click="{UpdateForm}">Apply</div>
	</div>
	{/if}

    {#if cardUpdate && formUpdate || !cardUpdate && formUpdate}

	<div class="fulldesc">
		<slot name="fulldesc">
			<span class="missing">Unknown description</span>
		</slot>
	</div>

	<div class="wages">
		<slot name="wages">
			<span class="missing">Unknown description</span>
		</slot>
	</div>

	<div class="place">
		<slot name="place">
			<span class="missing">Unknown description</span>
		</slot>
	</div>

	<div class="id">
		<slot name="id">
			<span class="missing">Unknown</span>
		</slot>
	</div>

	<form on:submit class="FormComponent">
		<div class="input-field">
		  <label for="first_name">Name</label>
		  <input type="text" id="first_name" bind:value={name}/>
		</div>

		<div class="input-field">
			<label for="last_name">Address</label>
			<input type="text" id="last_name" bind:value={address}/>
		</div>
		
		<div class="input-field">
		  <label for="email">Description</label>
		  <input type="email" id="email" bind:value={description}/>
		</div>
		
		<div class="input-field">
		  <label for="message">URL</label>
		  <textarea id="message" bind:value={url}></textarea>
		</div>
		
		<div class="form-buttons">
			<div class="button" on:click="{UpdateCard}" on:click="{UpdateForm}">See less</div>
			<div class="button" on:click="{submitForm}">Submit</div>
		</div>
	</form>
	{/if}

</article> -->