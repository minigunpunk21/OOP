import { Repository } from './repository';
import { FileChange } from './fileChange';

export class Commit {
    constructor(private repository: Repository) {}

    createCommit(message: string): void {
        const changes: FileChange[] = [];

        for (const [filePath, content] of this.repository.getFiles()) {
            changes.push(new FileChange(filePath, 'modified'));
        }

        console.log(`Commit created: ${message}`);
        console.log('Changes:', changes);
    }
}
