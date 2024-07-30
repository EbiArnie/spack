# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlStatisticsDescriptive(PerlPackage):
    """Module of basic descriptive statistical functions."""

    homepage = "https://metacpan.org/pod/Statistics::Descriptive"
    url = "https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Statistics-Descriptive-3.0801.tar.gz"

    maintainers("EbiArnie")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("3.0801", sha256="047b70a63fdcaa916168e0ff2d58e155e0ebbc68ed4ccbd73a7213dca3028f65")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))
    depends_on("perl-list-moreutils", type=("build", "run", "test"))

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use Statistics::Descriptive; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
