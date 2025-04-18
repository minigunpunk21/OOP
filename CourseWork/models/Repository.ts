import { Commit } from './Commit';
import { File } from './File';
import { Branch } from './Branch';

export class Repository {
    private commits: Commit[] = [];
    private files: File[] = [];
    private branches: Branch[] = [];
    
    constructor(
        public id: string,
        public name: string,
        public path: string,
        public ownerId: string,
        public lastUpdated: Date
    ) {}

    addFile(file: File): void {
        this.files.push(file);
    }

    addCommit(commit: Commit): void {
        this.commits.push(commit);
    }

    addBranch(branch: Branch): void {
        this.branches.push(branch);
    }

    getCommits(): Commit[] {
        return this.commits;
    }

    getFiles(): File[] {
        return this.files;
    }

    getBranches(): Branch[] {
        return this.branches;
    }
}
