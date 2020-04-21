import gitUtils
import fileUtils

original_repository_path = 'E:/git_history/hirescapes-front-end-original'
new_repository_path = 'E:/git_history/hirescapes-front-end'


def start_git_copy(src, dst):
    gitUtils.git_checkout_to_commit(original_repository_path, 'master')
    log_data = gitUtils.git_logs(src)
    fileUtils.reset_directory(dst)
    gitUtils.git_init(dst)
    for log in log_data:
        print(f'processing {log["id"]}')
        gitUtils.git_checkout_to_commit(src, log['id'])
        fileUtils.remove_files(new_repository_path)
        fileUtils.copy_files(original_repository_path, new_repository_path)
        gitUtils.git_commit(new_repository_path, log['email'], log['message'], log['date'])


if __name__ == '__main__':
    start_git_copy(original_repository_path, new_repository_path)
