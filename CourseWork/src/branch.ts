import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

export class Branch {
    constructor(private repoPath: string) {}

    async create(name: string): Promise<void> {
        await execAsync(`git branch ${name}`, { cwd: this.repoPath });
        console.log(`Branch ${name} created`);
    }

    async checkout(name: string): Promise<void> {
        await execAsync(`git checkout ${name}`, { cwd: this.repoPath });
        console.log(`Switched to branch ${name}`);
    }
}
