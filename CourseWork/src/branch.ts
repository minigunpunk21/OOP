import { Repository } from './repository';

export class Branch {
    private branches: string[] = [];
    private currentBranch: string = 'main';

    constructor(private repository: Repository) {
        this.branches.push(this.currentBranch);
    }

    createBranch(name: string): void {
        if (!this.branches.includes(name)) {
            this.branches.push(name);
            console.log(`Branch created: ${name}`);
        } else {
            console.log(`Branch ${name} already exists.`);
        }
    }

    checkoutBranch(name: string): void {
        if (this.branches.includes(name)) {
            this.currentBranch = name;
            console.log(`Switched to branch: ${name}`);
        } else {
            console.log(`Branch ${name} does not exist.`);
        }
    }

    getCurrentBranch(): string {
        return this.currentBranch;
    }
}
