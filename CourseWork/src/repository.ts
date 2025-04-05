import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

export class Repository {
    constructor(private repoPath: string) {}

    async init(): Promise<void> {
        await execAsync('git init', { cwd: this.repoPath });
        console.log(`Initialized empty Git repository in ${this.repoPath}`);
    }

    async getStatus(): Promise<string> {
        const { stdout } = await execAsync('git status', { cwd: this.repoPath });
        return stdout;
    }

    async rollback(): Promise<void> {
        await execAsync('git reset --hard HEAD', { cwd: this.repoPath });
        console.log('Rolled back to the last commit');
    }
}
