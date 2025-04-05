import { exec } from 'child_process';
import { promisify } from 'util';
import { FileChange } from './fileChange'; // Добавьте этот импорт

const execAsync = promisify(exec);

export class Commit {
    constructor(private repoPath: string) {}

    async commit(message: string): Promise<void> {
        await execAsync(`git commit -m "${message}"`, { cwd: this.repoPath });
        console.log(`Committed changes: ${message}`);
    }

    async trackFileChanges(): Promise<FileChange[]> {
        const { stdout } = await execAsync('git status --porcelain', { cwd: this.repoPath });
        const changes: FileChange[] = [];

        stdout.split('\n').forEach(line => {
            const changeType = line[0] === 'A' ? 'added' : line[0] === 'M' ? 'modified' : line[0] === 'D' ? 'deleted' : null;
            if (changeType) {
                const filePath = line.slice(3).trim();
                changes.push(new FileChange(filePath, changeType));
            }
        });

        return changes;
    }
}
