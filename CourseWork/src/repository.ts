import { FileChange } from './fileChange';
import { hashString } from './utils';

export class Repository {
    private files: Map<string, string> = new Map(); // Хранит состояние файлов
    private history: string[] = []; // Хранит хэши коммитов
    private currentBranch: string = 'main';

    init(): void {
        this.files.clear();
        this.history = [];
        console.log('Initialized empty version control repository.');
    }

    addFile(filePath: string, content: string): void {
        this.files.set(filePath, content);
        console.log(`Added file: ${filePath}`);
    }

    modifyFile(filePath: string, content: string): void {
        if (this.files.has(filePath)) {
            this.files.set(filePath, content);
            console.log(`Modified file: ${filePath}`);
        }
    }

    deleteFile(filePath: string): void {
        if (this.files.has(filePath)) {
            this.files.delete(filePath);
            console.log(`Deleted file: ${filePath}`);
        }
    }

    getFiles(): Map<string, string> {
        return this.files;
    }

    commit(): string {
        const commitHash = hashString(JSON.stringify([...this.files]));
        this.history.push(commitHash);
        console.log(`Commit created: ${commitHash}`);
        return commitHash;
    }

    rollback(): void {
        if (this.history.length > 0) {
            this.history.pop();
            console.log('Rolled back to previous commit.');
        } else {
            console.log('No commits to roll back.');
        }
    }

    getHistory(): string[] {
        return this.history;
    }
}
