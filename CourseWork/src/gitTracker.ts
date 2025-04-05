import { Repository } from './repository';
import { Commit } from './commit';
import { Branch } from './branch';
import { FileChange } from './fileChange';

export class GitTracker {
    private repository: Repository;
    private commit: Commit;
    private branch: Branch;

    constructor(repoPath: string) {
        this.repository = new Repository(repoPath);
        this.commit = new Commit(repoPath);
        this.branch = new Branch(repoPath);
    }

    async initRepository(): Promise<void> {
        await this.repository.init();
    }

    async trackFileChanges(): Promise<FileChange[]> {
        return await this.commit.trackFileChanges();
    }

    async commitChanges(message: string): Promise<void> {
        await this.commit.commit(message);
    }

    async getStatus(): Promise<string> {
        return await this.repository.getStatus();
    }

    async createBranch(name: string): Promise<void> {
        await this.branch.create(name);
    }

    async checkoutBranch(name: string): Promise<void> {
        await this.branch.checkout(name);
    }

    async rollback(): Promise<void> {
        await this.repository.rollback();
    }
}
