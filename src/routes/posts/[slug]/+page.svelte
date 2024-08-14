<script lang="ts">
	// page.ts -> 클라이언트측 코드
	// page.server.ts -> 서버측 코드
	export let data;
	console.log('????')
</script>

<svelte:head>
	<title>{data.meta.title}</title>
	<meta property="og:type" content="article" />
	<meta property="og:title" content={data.meta.title} />
</svelte:head>

<article class="container flex flex-col pt-10 space-y-10 items-center">
	<div>
		<h1>{data.meta.title}</h1>
		<p>Published at {data.meta.date}</p>
	</div>

	<div class="space-x-4">
		{#each data.meta.categories as category}
			<span class="border rounded-xl py-2 px-4 bg-slate-200">&num;{category}</span>
		{/each}
	</div>

	<div class="text-lg border">
		<svelte:component this={data.content} />
	</div>
</article>
