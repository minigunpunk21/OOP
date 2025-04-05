import { FileChange } from './fileChange';

export class Repository {
    private files: Map<string, string> = new Map(); // Хранит состояние файлов

    init(): void {
        this.files.clear();
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
}
