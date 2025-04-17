import { Repository } from '../models/Repository';
import { Commit } from '../models/Commit';
import { File } from '../models/File';
import { Branch } from '../models/Branch';

export class RepositoryService {
    private repositories: Repository[] = [];

    createRepository(name: string, path: string, ownerId: string): Repository {
        const repository = new Repository(
            (this.repositories.length + 1).toString(),
            name,
            path,
            ownerId,
            new Date()
        );
        this.repositories.push(repository);
        return repository;
    }

    getRepository(id: string): Repository | undefined {
        return this.repositories.find(repo => repo.id === id);
    }
}
