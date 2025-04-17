export class File {
    constructor(
        public id: string,
        public path: string,
        public repositoryId: string,
        public status: 'added' | 'modified' | 'deleted'
    ) {}
}
