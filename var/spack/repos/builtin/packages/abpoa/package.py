# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install abpoa
#
# You can edit this file again by typing:
#
#     spack edit abpoa
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Abpoa(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/yangao07/abPOA/releases/download/v1.4.1/abPOA-v1.4.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("1.4.1", sha256="54b1f5cfd94fb5894e189d9e099f8158051411bcbcc9ba2d77478cfb9221dde1")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    # env: set avx2 1

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make("install")
