export class FileChange {
    constructor(
        public filePath: string,
        public changeType: 'added' | 'modified' | 'deleted'
    ) {}
}
