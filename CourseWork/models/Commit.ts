export class Commit {
    constructor(
        public id: string,
        public hash: string,
        public repositoryId: string,
        public author: string,
        public createdAt: Date,
        public message: string
    ) {}
}
