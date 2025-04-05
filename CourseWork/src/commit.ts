import { Repository } from './repository';

export class Commit {
    constructor(private repository: Repository) {}

    createCommit(message: string): void {
        const commitHash = this.repository.commit();
        console.log(`Commit message: ${message}`);
        console.log(`Commit hash: ${commitHash}`);
    }
}
