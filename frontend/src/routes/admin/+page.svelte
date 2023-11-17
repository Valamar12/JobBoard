<h1>ADMIN</h1>
<script>
    import UpdateForm from './UpdateForm.svelte';
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    // TO DO
    // List all adverts that has been published by the specific connected admin

    let updateForm = false;
    let replyForm = false;

    function showForm() {
        updateForm = true;
    }

    function showReplyForm() {
        replyForm = true;
    }

    function sendAnswer(app_id, advert_id, status) {

        const data = { "status": status, "advert": advert_id, "user": 1 };

        let confirmation = confirm("You are about to send a definitive answer to applicant. Are you sure?");
        if (confirmation) {
            console.log("OK")
            console.log(app_id)
            console.log(advert_id)
            fetch(`http://localhost:8000/api/application/update/${app_id}`, {
            method: 'PATCH',
            headers: {'Content-Type': 'application/json', 
            },
            body: JSON.stringify(data)
            })
            .then(response => {
                if (response.ok) {
                    console.log("Data sent and saved to the database.");
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
            })
        }

    }


    let adverts = [];

	onMount(async () => {
		const response = await fetch('http://localhost:8000/api/adverts');
		const jsonData = await response.json();
		adverts = jsonData;
        console.log(adverts);
        adverts.forEach((advert) => {
            console.log(advert.company)
        })
	});


    let applications = [];

    onMount(async () => {
		const response = await fetch('http://localhost:8000/api/application');
		const jsonData = await response.json();
		applications = jsonData;
        console.log(applications);
        // adverts.forEach((advert) => {
        //     console.log(advert.company)
        // })
	});


    console.log(applications)
    let title = "";
    let description = "";
    let experience = "";
    let salary = "";

    function createAdvert() {

        const data = { "title": title, "description": description, 
            	        "experience": experience, "salary": salary, "company": 1 };

        fetch(`http://localhost:8000/api/adverts/create`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json', 
            },
            body: JSON.stringify(data)
        })
        .then(response => {
        if (response.ok) {
            console.log("Data sent and saved to the database.");
        }
        return response.json();
        })
        .then(data => {
            console.log(data);
            adverts = [...adverts, data];
            // adverts.push(data);
            console.log(adverts)
        })
    }

    function updateAdvert(advert_id, company_id) {

        const data = { "title": title, "description": description, 
                    "experience": experience, "salary": salary, "company": company_id };

        fetch(`http://localhost:8000/api/adverts/update/${advert_id}`, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json', 
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                console.log("Data sent and saved to the database.");
            }
            return response.json();
        })
        // .then(data => {
        //     console.log(data);
        // })
    }

    function deleteAdvert(advert_id) {

        let confirmation = confirm(`Are you sure you want to delete advert?`);

        if (confirmation) {

            fetch(`http://localhost:8000/api/adverts/delete/${advert_id}`, {
                method: 'DELETE',
                headers: {'Content-Type': 'application/json', 
                }
            })
            .then(response => {
                if (response.status === 204) {
                    // The resource was successfully deleted.
                    console.log('Resource deleted successfully');
                } else if (response.status === 404) {
                    // The resource was not found.
                    console.error('Resource not found');
                } else {
                    // Handle other response statuses accordingly.
                    console.error('Failed to delete resource');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            })
        }
    }

    function showApplications(advert_id) {
        console.log(advert_id);
        console.log(applications);
        console.log(adverts);
        let advertApplications = applications.filter(application => application.advert.id === advert_id);
        console.log(advertApplications);
        return advertApplications.length;
    }

    function test() {
        window.location.href = '/'
    }

</script>

<head>
    <link rel="stylesheet" href="styles.css"/>
</head>
<section>

    <div class="button" on:click={createAdvert}>Publish new Advert</div>
    <form on:submit class="FormComponent">
        <div class="input-field">
            <label for="title">Title</label>
            <input type="text" id="title" bind:value={title} required/>
        </div>

        <div class="input-field">
            <label for="description">Description</label>
            <input type="text" id="description" bind:value={description} required/>
        </div>
        
        <div class="input-field">
            <label for="experience">Experience</label>
            <input type="text" id="experience" bind:value={experience} required/>
        </div>
        
        <div class="input-field">
            <label for="message">Salary</label>
            <input type="text" id="salary" bind:value={salary} required/>
        </div>
    </form>
    <h1>PUBLISHED ADVERTS</h1>
    <div class="advert-container"> 
	{#each adverts as advert (advert.id)}
        <article class="advert-card">
            <div><h2>{advert.title}</h2></div>
            <div><h2>{advert.company.name}</h2></div>
            <div><h2>{advert.description}</h2></div>
            <div><h2>{advert.experience}</h2></div>
            <div><h2>{advert.salary}€</h2></div>
            <div><h2>{advert.company.address}</h2></div>
            <div id="btn" on:click={test}><h2><strong>Applications:</strong> {showApplications(advert.id)}</h2></div>
            <div class="buttons">
                <div class="button" on:click={showForm}>Update Advert</div>
                <div id="dlt-btn" on:click={deleteAdvert(advert.id)}>Delete Advert</div>
            </div>
            {#if updateForm}
                <form on:submit class="FormComponent">
                    <div class="input-field">
                        <label for="title">Title</label>
                        <input type="text" id="title" bind:value={title}/>
                    </div>

                    <div class="input-field">
                        <label for="description">Description</label>
                        <input type="text" id="description" bind:value={description}/>
                    </div>
                    
                    <div class="input-field">
                        <label for="experience">Experience</label>
                        <input type="text" id="experience" bind:value={experience}/>
                    </div>
                    
                    <div class="input-field">
                        <label for="message">Salary</label>
                        <input type="text" id="salary" bind:value={salary}/>
                    </div>
                </form>
                <div class="button" on:click={updateAdvert(advert.id, advert.company.id)}>Update Advert</div>
            {/if}
        </article>
    {/each}
</div>
    <h1>APPLICATIONS</h1>
    <div class="advert-container"> 
        {#each applications as app (app.id)}
            <article class="advert-card">
                <div><h2>{app.advert.title}</h2></div>
                <div><h2>{app.advert.company.name}</h2></div>
                <div><h2><strong>Status:</strong> {app.status}</h2></div>
            
                {#if replyForm}
                    <div class="buttons"> 
                        <div class="button" on:click={sendAnswer(app.id, app.advert.id, "Reviewing")}>Reviewing</div>
                        <div class="button" on:click={sendAnswer(app.id, app.advert.id, "Rejected")}>Rejected</div>
                    </div>
                {/if}
                <div class="button" on:click={showReplyForm}>Reply to application</div>
            </article>
        {/each}
    </div>
</section>

<style>
    #btn {
        text-decoration: underline;
    }

    .card {
	width: 400px;
    /* height: 400px; */
	border-radius: 18px;
	box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
	padding: 1em;
	margin-bottom: 25px;
    }

    .buttons {
        margin-bottom: 15px;
    }
</style>