#include <stdio.h>
#include <unistd.h>

#define RUNNER_GID 1000
#define RUNNER_UID 1000

int main(int argc, char * argv[])
{
  // must be root
  if (getuid() != (uid_t) 0) {
    fprintf(stderr, "Must be root to execute this!\n");
    return -1;
  }

  if (argc == 1) {
    fprintf(stderr, "Usage: %s [command]\n", argv[0]);
    return -1;
  }

  // set uid and gid
  setgid(RUNNER_GID);
  setuid(RUNNER_UID);

  // run!
  argv++;
  execvp(*argv, argv);
}
