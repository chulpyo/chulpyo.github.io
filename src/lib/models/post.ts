export interface BlogPost {
    slug: string;
    title: string;
    content: string;
};

export interface BlogPostContainer {
    post: BlogPost;
}