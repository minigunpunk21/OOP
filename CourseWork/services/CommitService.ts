import { Commit } from '../models/Commit';
import { Repository } from '../models/Repository';
import { hashString } from '../utils/hash';

export class CommitService {
    createCommit(repository: Repository, author: string, message: string): Commit {
        const commitHash = hashString(message + Date.now().toString());
        const commit = new Commit(
            (repository.getCommits().length + 1).toString(),
            commitHash,
            repository.id,
            author,
            new Date(),
            message
        );
        repository.addCommit(commit);
        return commit;
    }
}
