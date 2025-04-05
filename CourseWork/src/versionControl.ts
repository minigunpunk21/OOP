import { Repository } from './repository';
import { Commit } from './commit';
import { Branch } from './branch';

export class VersionControl {
    private repository: Repository;
    private commit: Commit;
    private branch: Branch;

    constructor() {
        this.repository = new Repository();
        this.commit = new Commit(this.repository);
        this.branch = new Branch(this.repository);
    }

    initRepository(): void {
        this.repository.init();
    }

    addFile(filePath: string, content: string): void {
        this.repository.addFile(filePath, content);
    }

    modifyFile(filePath: string, content: string): void {
        this.repository.modifyFile(filePath, content);
    }

    deleteFile(filePath: string): void {
        this.repository.deleteFile(filePath);
    }

    createCommit(message: string): void {
        this.commit.createCommit(message);
    }

    createBranch(name: string): void {
        this.branch.createBranch(name);
    }

    checkoutBranch(name: string): void {
        this.branch.checkoutBranch(name);
    }

    getCurrentBranch(): string {
        return this.branch.getCurrentBranch();
    }
}
