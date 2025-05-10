export class Branch {
    constructor(
        public id: string,
        public name: string,
        public repositoryId: string,
        public lastCommitId: string
    ) {}
}
