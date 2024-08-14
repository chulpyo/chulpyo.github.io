// import adapter from '@sveltejs/adapter-auto';
import fs from 'fs';
import adapter from "@sveltejs/adapter-static";
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

import { mdsvex } from 'mdsvex';


const base_path = './src/posts/'
const base_uri = '/posts/'
let files = fs.readdirSync(`${base_path}`).map((item) => {
	return `${base_uri}${item.replace('.md', '')}`;
});

/** @type {import('mdsvex').MdsvexOptions} */
const mdsvexOptions = {
	extensions: ['.md', 'svx'],
}

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// md 페이지 랜더링을 위하여 extensions 추가
	extensions: ['.svelte', '.svx', '.md'],
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: [vitePreprocess(), mdsvex(mdsvexOptions)],

	kit: {
		// adapter-auto only supports some environments, see https://kit.svelte.dev/docs/adapter-auto for a list.
		// If your environment is not supported, or you settled on a specific environment, switch out the adapter.
		// See https://kit.svelte.dev/docs/adapters for more information about adapters.
		adapter: adapter(),

		// 다이나믹 라우팅을 스태틱 랜더링 하기위한 설정
		prerender: {
			crawl: true,
			entries: [
				'/api/posts',
				'/posts',
				...files
			]
		}
	}
};

export default config;
